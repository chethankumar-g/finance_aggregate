import React from 'react';
import { Line } from 'react-chartjs-2';
import { Paper, Typography } from '@material-ui/core';

const TransactionChart = ({ transactions }) => {
  const data = {
    labels: transactions.map(t => t.step),
    datasets: [
      {
        label: 'Transaction Amount',
        data: transactions.map(t => t.amount),
        fill: false,
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1
      }
    ]
  };

  return (
    <Paper style={{ padding: '20px', marginTop: '20px' }}>
      <Typography variant="h6" gutterBottom>
        Transaction History
      </Typography>
      <Line data={data} />
    </Paper>
  );
};

export default TransactionChart;