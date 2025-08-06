CREATE TABLE cpe_data (
	id INTEGER NOT NULL, 
	cpe_title VARCHAR NOT NULL, 
	cpe_22_uri TEXT NOT NULL, 
	cpe_23_uri TEXT NOT NULL, 
	reference_links JSON NOT NULL, 
	cpe_22_deprecation_date DATE, 
	cpe_23_deprecation_date DATE, 
	PRIMARY KEY (id)
);
CREATE INDEX ix_cpe_data_cpe_22_deprecation_date ON cpe_data (cpe_22_deprecation_date);
CREATE INDEX ix_cpe_data_cpe_22_uri ON cpe_data (cpe_22_uri);
CREATE INDEX ix_cpe_data_cpe_23_deprecation_date ON cpe_data (cpe_23_deprecation_date);
CREATE INDEX ix_cpe_data_cpe_23_uri ON cpe_data (cpe_23_uri);
CREATE INDEX ix_cpe_data_cpe_title ON cpe_data (cpe_title);
