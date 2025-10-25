// src/components/Navbar/Navbar.js

import React from 'react';
import { Link } from 'react-router-dom';
import { AppBar, Toolbar, Typography, Button, Box } from '@mui/material';

const Navbar = () => {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            <Link to="/" style={{ textDecoration: 'none', color: 'inherit' }}>
              IAM Project
            </Link>
          </Typography>
          <Button color="inherit" component={Link} to="/users">Users</Button>
          <Button color="inherit" component={Link} to="/services">Services</Button>
          <Button color="inherit" component={Link} to="/roles">Roles</Button>
          <Button color="inherit" component={Link} to="/accesses">Accesses</Button>
        </Toolbar>
      </AppBar>
    </Box>
  );
};

export default Navbar;