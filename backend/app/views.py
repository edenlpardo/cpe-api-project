#views.py
from flask import Blueprint, jsonify, request
from sqlalchemy import or_, and_
from sqlalchemy.orm import load_only
from .models import db, CPE
from datetime import datetime

api = Blueprint('api', __name__)

def parse_date(date_str):
    """
    Safely parse a date string in 'YYYY-MM-DD' format.
    Returns None if parsing fails.
    """
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None

@api.route('/api/cpes', methods=['GET'])
def get_all_cpes():
    """
    Returns a paginated list of all CPE records.
    Optional query params: page (default 1), limit (default 10).
    """
    try:
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))

        pagination = CPE.query.order_by(CPE.id).paginate(page=page, per_page=limit, error_out=False)
        cpe_results = []

        for cpe in pagination.items:
            cpe_results.append({
                'id': cpe.id,
                'cpe_title': cpe.cpe_title,
                'cpe_22_uri': cpe.cpe_22_uri,
                'cpe_23_uri': cpe.cpe_23_uri,
                'reference_links': cpe.reference_links or [],
                'cpe_22_deprecation_date': cpe.cpe_22_deprecation_date,
                'cpe_23_deprecation_date': cpe.cpe_23_deprecation_date,
            })

        return jsonify({
            'page': pagination.page,
            'limit': pagination.per_page,
            'total': pagination.total,
            'data': cpe_results
        })
    except Exception as e:
        return jsonify({"error": f"Failed to retrieve CPEs: {str(e)}"}), 400

@api.route('/api/cpes/search', methods=['GET'])
def search_cpes():
    """
    Search CPE entries by title, 2.2 URI, 2.3 URI, and/or a deprecation date.
    All parameters are optional. If deprecation date is provided,
    it returns CPEs deprecated before that date.
    """
    try:
        # Get query parameters and strip whitespace
        cpe_title = request.args.get('cpe_title', '').strip()
        cpe_22_uri = request.args.get('cpe_22_uri', '').strip()
        cpe_23_uri = request.args.get('cpe_23_uri', '').strip()
        deprecation_date_str = request.args.get('deprecation_date', '').strip()
        deprecation_date = parse_date(deprecation_date_str) if deprecation_date_str else None

        # Build filters based on provided parameters
        filters = []
        if cpe_title:
            filters.append(CPE.cpe_title.ilike(f"%{cpe_title}%"))
        if cpe_22_uri:
            filters.append(CPE.cpe_22_uri.ilike(f"%{cpe_22_uri}%"))
        if cpe_23_uri:
            filters.append(CPE.cpe_23_uri.ilike(f"%{cpe_23_uri}%"))
        if deprecation_date:
            filters.append(or_(
                and_(CPE.cpe_22_deprecation_date != None, CPE.cpe_22_deprecation_date < deprecation_date),
                and_(CPE.cpe_23_deprecation_date != None, CPE.cpe_23_deprecation_date < deprecation_date),
            ))

        # Start query and apply filters
        # Load only for performance
        query = CPE.query.options(load_only(
            CPE.id,
            CPE.cpe_title,
            CPE.cpe_22_uri,
            CPE.cpe_23_uri,
            CPE.reference_links,
            CPE.cpe_22_deprecation_date,
            CPE.cpe_23_deprecation_date
        ))

        if filters:
            query = query.filter(*filters)

        cpe_results = query.order_by(CPE.id).all()

        # Format results for JSON response
        data = []
        for cpe in cpe_results:
            data.append({
                'id': cpe.id,
                'cpe_title': cpe.cpe_title,
                'cpe_22_uri': cpe.cpe_22_uri,
                'cpe_23_uri': cpe.cpe_23_uri,
                'reference_links': cpe.reference_links or [],
                'cpe_22_deprecation_date': cpe.cpe_22_deprecation_date.isoformat() if cpe.cpe_22_deprecation_date else None,
                'cpe_23_deprecation_date': cpe.cpe_23_deprecation_date.isoformat() if cpe.cpe_23_deprecation_date else None,
            })
        return jsonify({'data': data})
    
    except Exception as e:
        return jsonify({"error": f"Search failed: {str(e)}"}), 400
