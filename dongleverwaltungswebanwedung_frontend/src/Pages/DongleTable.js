import React, { useEffect, useState } from 'react';
import axios from 'axios';

const DongleTable = () => {
  const [employees, setDongles] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await axios.get('http://127.0.0.1:8000/homepage/');
      setDongles(response.data.Dongle);
    };

    fetchData();
  }, []);

  return (
    <table>
      <thead>
        <tr>
          <th>Lfd.Nr</th>
          <th>Serien-Nr</th>
          <th>Name</th>
        </tr>
      </thead>
      <tbody>
        {employees.map(employee => (
          <tr>
            <td>{employee.lfd_nr_field}</td>
            <td>{employee.serien_nr}</td>
            <td>{employee.name}</td>
          </tr>
        ))}
      </tbody>
    </table>  );
};

export default DongleTable;