import React from 'react';
import { Line, Bar } from 'react-chartjs-2';

const Charts = ({ data }) => {
    const lineChartData = {
        labels: data.map(item => item.date),
        datasets: [
            {
                label: 'Transaction Amount',
                data: data.map(item => item.amount),
                borderColor: 'rgba(75,192,192,1)',
                fill: false,
            },
        ],
    };

    const barChartData = {
        labels: data.map(item => item.category),
        datasets: [
            {
                label: 'Total Amount by Category',
                data: data.reduce((acc, item) => {
                    acc[item.category] = (acc[item.category] || 0) + item.amount;
                    return acc;
                }, {}),
                backgroundColor: 'rgba(75,192,192,0.5)',
            },
        ],
    };

    return (
        <div>
            <h2>Transaction Amount Over Time</h2>
            <Line data={lineChartData} />
            <h2>Total Amount by Category</h2>
            <Bar data={barChartData} />
        </div>
    );
};

export default Charts;