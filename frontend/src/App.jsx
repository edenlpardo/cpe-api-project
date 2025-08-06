import React from 'react';
import CPETable from './components/CPETable';
import { Container, Typography } from '@mui/material';

function App() {
  return (
    <Container maxWidth="xl">
      <Typography variant="h4" gutterBottom sx={{ my: 4 }}>
        CPE Data Viewer
      </Typography>
      <CPETable />
    </Container>
  );
}

export default App;
