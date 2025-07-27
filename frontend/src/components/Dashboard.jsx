import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';

const Dashboard = () => {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get('/api/transactions'); // Adjust the endpoint as necessary
                setData(response.data);
            } catch (error) {
                console.error('Error fetching data:', error);
            } finally {
                setLoading(false);
            }
        };

        fetchData();
    }, []);

    const chartData = {
        labels: data.map(item => item.category), // Assuming category is a field in your data
        datasets: [
            {
                label: 'Transaction Amount',
                data: data.map(item => item.amount), // Assuming amount is a field in your data
                backgroundColor: 'rgba(75, 192, 192, 0.6)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1,
            },
        ],
    };

    return (
        <div>
            <h2>Financial Dashboard</h2>
            {loading ? (
                <p>Loading...</p>
            ) : (
                <Line data={chartData} />
            )}
        </div>
    );
};

export default Dashboard;