import React from 'react';
import { AppBar, Toolbar, Typography, Button } from '@material-ui/core';
import { useHistory } from 'react-router-dom';

const Header = () => {
  const history = useHistory();
  
  const handleLogout = () => {
    localStorage.removeItem('token');
    history.push('/login');
  };

  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" style={{ flexGrow: 1 }}>
          Financial Dashboard
        </Typography>
        <Button color="inherit" onClick={handleLogout}>
          Logout
        </Button>
      </Toolbar>
    </AppBar>
  );
};

export default Header;