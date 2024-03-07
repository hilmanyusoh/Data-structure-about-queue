const express = require('express');
const bodyParser = require('body-parser');
const { Pool } = require('pg');

const app = express();
const port = 3000;

const pool = new Pool({
  user: 'your_username',
  host: 'localhost',
  database: 'your_database',
  password: 'your_password',
  port: 5432,
});

app.use(bodyParser.json());

app.post('/addPersonToQueue', (req, res) => {
  const { name, order } = req.body;
  const query = 'INSERT INTO queue (name, order) VALUES ($1, $2)';
  pool.query(query, [name, order], (error, results) => {
    if (error) {
      res.status(500).json({ error: 'Error adding person to queue' });
    } else {
      res.status(200).json({ message: 'Person added to queue successfully' });
    }
  });
});

// เพิ่มจุดปลายทางเพิ่มเติมสำหรับการดำเนินการ CRUD ตามต้องการ

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
