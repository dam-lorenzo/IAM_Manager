// src/components/Users/UsersTable.js
import React, { useState, useEffect } from 'react';
import { apiGet, apiPut } from '../../apiClient/apiService';
import {
  Container,
  Typography,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  IconButton,
  CircularProgress,
  Alert
} from '@mui/material';

import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import { api_search_users, api_update_users } from '../../settings/settings'; 

function UsersTable() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    apiGet(api_search_users)
  }, []);

  const handleEdit = (userId) => {
    apiPut(api_update_users + '/' + userId)
  };

  // const handleDelete = (userId) => {
  //   // Aquí iría la lógica para mostrar una confirmación y eliminar el usuario
  // };
  // handleAdd (?)
  if (loading) {
    return (
      <Container sx={{ display: 'flex', justifyContent: 'center', mt: 4 }}>
        <CircularProgress />
      </Container>
    );
  }

  if (error) {
    return (
      <Container sx={{ mt: 4 }}>
        <Alert severity="error">empty database: {error}</Alert>
      </Container>
    );
  }
  return (
    <Container sx={{ mt: 4 }}> {}
      <Typography variant="h4" gutterBottom>
        User managment
      </Typography>
      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>ID</TableCell>
              <TableCell>Nombre</TableCell>
              <TableCell>Email</TableCell>
              <TableCell align="right">Acciones</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {users.map((user) => (
              <TableRow key={user.id}>
                <TableCell>{user.id}</TableCell>
                <TableCell>{user.name}</TableCell>
                <TableCell>{user.email}</TableCell>
                <TableCell align="right">
                  <IconButton color="primary" onClick={handleEdit(user.id)}>
                    <EditIcon />
                  </IconButton>
                  <IconButton color="error">
                    <DeleteIcon />
                  </IconButton>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Container>
  );
};

export default UsersTable;