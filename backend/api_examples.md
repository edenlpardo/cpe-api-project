# API Example Requests and Responses

## Get ALL CPE Entries:
    --> htttp
    GET /api/cpes

    --> Response
        {
    "data": [
        {
        "cpe_22_deprecation_date": null,
        "cpe_22_uri": "cpe:/a:%240.99_kindle_books_project:%240.99_kindle_books:6::~~~android~~",
        "cpe_23_deprecation_date": null,
        "cpe_23_uri": "cpe:2.3:a:\\$0.99_kindle_books_project:\\$0.99_kindle_books:6:*:*:*:*:android:*:*",
        "cpe_title": "$0.99 Kindle Books project $0.99 Kindle Books (aka com.kindle.books.for99) for android 6.0",
        "id": 1,
        "reference_links": [
            "https://play.google.com/store/apps/details?id=com.kindle.books.for99",
            "https://docs.google.com/spreadsheets/d/1t5GXwjw82SyunALVJb2w0zi3FoLRIkfGPc7AMjRF0r4/edit?pli=1#gid=1053404143"
        ]
        },
        ...
        {
        "cpe_22_deprecation_date": null,
        "cpe_22_uri": "cpe:/a:%40thi.ng%2fegf_project:%40thi.ng%2fegf:0.3.2::~~~node.js~~",
        "cpe_23_deprecation_date": null,
        "cpe_23_uri": "cpe:2.3:a:\\@thi.ng\\/egf_project:\\@thi.ng\\/egf:0.3.2:*:*:*:*:node.js:*:*",
        "cpe_title": "@thi.ng/egf Project @thi.ng/egf 0.3.2 for Node.js",
        "id": 10,
        "reference_links": [
            "https://github.com/thi-ng/umbrella/security/advisories/GHSA-rj44-gpjc-29r7",
            "https://www.npmjs.com/package/@thi.ng/egf"
        ]
        }
    ],
    "limit": 10,
    "page": 1,
    "total": 1447777
    }

## Get ALL CPE Entries (with parameters):

    --> http
    GET /api/cpes?page=700002&limit=2

    --> Response
        {
    "data": [
        {
        "cpe_22_deprecation_date": null,
        "cpe_22_uri": "cpe:/a:wptools_project:wptools:1.08::~~~wordpress~~",
        "cpe_23_deprecation_date": null,
        "cpe_23_uri": "cpe:2.3:a:wptools_project:wptools:1.08:*:*:*:*:wordpress:*:*",
        "cpe_title": "WPTools Project WPTools 1.08 for WordPress",
        "id": 1400003,
        "reference_links": [
            "https://plugins.trac.wordpress.org/browser/wptools/#tags",
            "https://wordpress.org/plugins/wptools/",
            "https://wpscan.com/vulnerability/c2a9cf01-051a-429a-82ca-280885114b5a"
        ]
        },
        {
        "cpe_22_deprecation_date": null,
        "cpe_22_uri": "cpe:/a:wptools_project:wptools:1.09::~~~wordpress~~",
        "cpe_23_deprecation_date": null,
        "cpe_23_uri": "cpe:2.3:a:wptools_project:wptools:1.09:*:*:*:*:wordpress:*:*",
        "cpe_title": "WPTools Project WPTools 1.09 for WordPress",
        "id": 1400004,
        "reference_links": [
            "https://plugins.trac.wordpress.org/browser/wptools/#tags",
            "https://wordpress.org/plugins/wptools/",
            "https://wpscan.com/vulnerability/c2a9cf01-051a-429a-82ca-280885114b5a"
        ]
        }
    ],
    "limit": 2,
    "page": 700002,
    "total": 1447777
    }

## Search CPEs:

### Search by title:

    --> http
    GET /api/cpes/search?cpe_title=WPTools%20Project%20WPTools%201.08%20for%20WordPress

    --> Response
            {
    "data": [
        {
        "cpe_22_deprecation_date": null,
        "cpe_22_uri": "cpe:/a:wptools_project:wptools:1.08::~~~wordpress~~",
        "cpe_23_deprecation_date": null,
        "cpe_23_uri": "cpe:2.3:a:wptools_project:wptools:1.08:*:*:*:*:wordpress:*:*",
        "cpe_title": "WPTools Project WPTools 1.08 for WordPress",
        "id": 1400003,
        "reference_links": [
            "https://plugins.trac.wordpress.org/browser/wptools/#tags",
            "https://wordpress.org/plugins/wptools/",
            "https://wpscan.com/vulnerability/c2a9cf01-051a-429a-82ca-280885114b5a"
        ]
        }
    ]
    }

### Search by CPE 22 URI:

    --> http
    GET /api/cpes/search?cpe_22_uri=cpe:/a:wptools_project:wptools:1.08::~~~wordpress~~

    --> Reponse:
        {
    "data": [
        {
        "cpe_22_deprecation_date": null,
        "cpe_22_uri": "cpe:/a:wptools_project:wptools:1.08::~~~wordpress~~",
        "cpe_23_deprecation_date": null,
        "cpe_23_uri": "cpe:2.3:a:wptools_project:wptools:1.08:*:*:*:*:wordpress:*:*",
        "cpe_title": "WPTools Project WPTools 1.08 for WordPress",
        "id": 1400003,
        "reference_links": [
            "https://plugins.trac.wordpress.org/browser/wptools/#tags",
            "https://wordpress.org/plugins/wptools/",
            "https://wpscan.com/vulnerability/c2a9cf01-051a-429a-82ca-280885114b5a"
        ]
        }
    ]
    }

### Search by CPE 23 URI:

    --> http
    GET /api/cpes/search?cpe_23_uri=cpe:2.3:a:wptools_project:wptools:1.08:*:*:*:*:wordpress:*:*

    --> Response:
        {
    "data": [
        {
        "cpe_22_deprecation_date": null,
        "cpe_22_uri": "cpe:/a:wptools_project:wptools:1.08::~~~wordpress~~",
        "cpe_23_deprecation_date": null,
        "cpe_23_uri": "cpe:2.3:a:wptools_project:wptools:1.08:*:*:*:*:wordpress:*:*",
        "cpe_title": "WPTools Project WPTools 1.08 for WordPress",
        "id": 1400003,
        "reference_links": [
            "https://plugins.trac.wordpress.org/browser/wptools/#tags",
            "https://wordpress.org/plugins/wptools/",
            "https://wpscan.com/vulnerability/c2a9cf01-051a-429a-82ca-280885114b5a"
        ]
        }
    ]
    }


### Search by deprecation date:

    --> http
    GET /api/cpes/search?deprecation_date=2022-07-10

    --> Response
        {
    "data": [
        {
        "cpe_22_deprecation_date": "2021-06-10",
        "cpe_22_uri": "cpe:/a:100plus:101eip:200925",
        "cpe_23_deprecation_date": "2021-06-10",
        "cpe_23_uri": "cpe:2.3:a:100plus:101eip:200925:*:*:*:*:*:*:*",
        "cpe_title": "100plus 101EIP 200925",
        "id": 380,
        "reference_links": [
            "https://www.twcert.org.tw/tw/cp-132-4755-bd590-1.html",
            "https://www.100plus.com/",
            "https://github.com/CVEProject/cvelist/blob/master/2021/32xxx/CVE-2021-32539.json"
        ]
        },
        {
        "cpe_22_deprecation_date": "2020-05-11",
        "cpe_22_uri": "cpe:/a:1password:1password:3.0:-:~~~mac_os_x~~",
        "cpe_23_deprecation_date": "2020-05-11",
        "cpe_23_uri": "cpe:2.3:a:1password:1password:3.0:-:*:*:*:mac_os_x:*:*",
        "cpe_title": "1Password 3.0 - for Mac Os X",
        "id": 2498,
        "reference_links": [
            "https://app-updates.agilebits.com/product_history/OPM4"
        ]
        },
        {
        "cpe_22_deprecation_date": "2010-12-28",
        "cpe_22_uri": "cpe:/a:3com:tippingpoint_ips:-",
        "cpe_23_deprecation_date": "2010-12-28",
        "cpe_23_uri": "cpe:2.3:a:3com:tippingpoint_ips:-:*:*:*:*:*:*:*",
        "cpe_title": "3Com TippingPoint IPS",
        "id": 4239,
        "reference_links": []
        }
        ...