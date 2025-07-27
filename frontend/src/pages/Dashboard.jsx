import React, { useState, useEffect } from 'react';
import { Container, Grid, Paper, Typography } from '@material-ui/core';
import { getTransactions } from '../services/api';
import Header from '../components/Header';
import TransactionChart from '../components/TransactionChart';

const Dashboard = () => {
  const [transactions, setTransactions] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await getTransactions();
        setTransactions(response.data);
      } catch (error) {
        console.error('Error fetching transactions:', error);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <>
      <Header />
      <Container maxWidth="lg" style={{ marginTop: '20px' }}>
        <Grid container spacing={3}>
          <Grid item xs={12}>
            <Paper style={{ padding: '20px' }}>
              <Typography variant="h5" gutterBottom>
                Financial Overview
              </Typography>
              <Typography variant="body1">
                Total Transactions: {transactions.length}
              </Typography>
            </Paper>
          </Grid>
          <Grid item xs={12}>
            <TransactionChart transactions={transactions} />
          </Grid>
        </Grid>
      </Container>
    </>
  );
};

export default Dashboard;