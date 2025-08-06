import React, { useState, useEffect, useCallback } from 'react';
import axios from 'axios';
import {
  Table, TableBody, TableCell, TableContainer, TableHead, TableRow,
  TextField, Paper, TablePagination, CircularProgress
} from '@mui/material';
import ReferencePopover from './ReferencePopover';
import { formatDate } from '../utils/formatDate';

const CPE_API_BASE = 'http://127.0.0.1:5000/api/cpes';

const CPETable = () => {
  const [data, setData] = useState([]);
  const [filters, setFilters] = useState({
    cpe_title: '',
    cpe_22_uri: '',
    cpe_23_uri: '',
    deprecation_date: ''
  });
  const [page, setPage] = useState(0); // zero-based for pagination component
  const [limit, setLimit] = useState(15);
  const [total, setTotal] = useState(0);
  const [loading, setLoading] = useState(false);

  const fetchData = useCallback(async () => {
  setLoading(true);

  try {
    if (
      filters.cpe_title ||
      filters.cpe_22_uri ||
      filters.cpe_23_uri ||
      filters.deprecation_date
    ) {
      const { data } = await axios.get(`${CPE_API_BASE}/search`, {
        params: {
          ...(filters.cpe_title && { cpe_title: filters.cpe_title }),
          ...(filters.cpe_22_uri && { cpe_22_uri: filters.cpe_22_uri }),
          ...(filters.cpe_23_uri && { cpe_23_uri: filters.cpe_23_uri }),
          ...(filters.deprecation_date && { deprecation_date: filters.deprecation_date }),
        },
      });

      setData(data.data);
      setTotal(data.data.length);
    } else {
      const { data } = await axios.get(`${CPE_API_BASE}?page=${page + 1}&limit=${limit}`);
      setData(data.data);
      setTotal(data.total);
    }
  } catch (err) {
    console.error('Error fetching CPE data:', err);
  }

  setLoading(false);
  }, [filters, page, limit]);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  const handleChangePage = (event, newPage) => setPage(newPage);
  const handleChangeRowsPerPage = (event) => {
    setLimit(parseInt(event.target.value, 10));
    setPage(0);
  };

  const handleFilterChange = (field) => (e) => {
    setFilters(prev => ({ ...prev, [field]: e.target.value }));
    setPage(0);
  };

  return (
    <Paper sx={{ padding: 2 }}>
      {loading ? <CircularProgress /> : (
        <TableContainer>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell><TextField label="Title" variant="standard" fullWidth onChange={handleFilterChange('cpe_title')} /></TableCell>
                <TableCell><TextField label="URL_22" variant="standard" fullWidth onChange={handleFilterChange('cpe_22_uri')} /></TableCell>
                <TableCell><TextField label="URL_23" variant="standard" fullWidth onChange={handleFilterChange('cpe_23_uri')} /></TableCell>
                <TableCell><TextField label="Deprecated Date 22" variant="standard" fullWidth placeholder="MM-DD-YYYY" onChange={handleFilterChange('deprecation_date')} /></TableCell>
                <TableCell>Deprecation Date 2.3</TableCell>
                <TableCell>References</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {data.map(row => (
                <TableRow key={row.id}>
                  <TableCell title={row.cpe_title}>{row.cpe_title}</TableCell>
                  <TableCell>{row.cpe_22_uri}</TableCell>
                  <TableCell>{row.cpe_23_uri}</TableCell>
                  <TableCell>{formatDate(row.cpe_22_deprecation_date)}</TableCell>
                  <TableCell>{formatDate(row.cpe_23_deprecation_date)}</TableCell>
                  <TableCell><ReferencePopover references={row.reference_links} /></TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      )}
      <TablePagination
        component="div"
        count={total}
        page={page}
        onPageChange={handleChangePage}
        rowsPerPage={limit}
        onRowsPerPageChange={handleChangeRowsPerPage}
        rowsPerPageOptions={[15, 25, 50]}
      />
    </Paper>
  );
};

export default CPETable;
