import React from 'react';

const CustomTable = ({ data }) => {
  return (
    <table>
      <thead>
        <tr>
          <th>lfd_nr</th>
          <th>serien_nr</th>
          <th>name</th>
          <th>gueltig_von</th>
          <th>gueltig_bis</th>
          <th>projekt_produkt</th>
          <th>standort</th>
          <th>haendler</th>
          <th>datum_letzte_aenderung</th>
          <th>datum_erstausgabe</th>
          <th>benutzer_firmcode</th>
        </tr>
      </thead>
      <tbody>
        {data.map((row) => (
          <tr key={row.lfd_nr}>
            <td>{row.lfd_nr}</td>
            <td>{row.serien_nr}</td>
            <td>{row.name}</td>
            <td>{row.gueltig_von}</td>
            <td>{row.gueltig_bis}</td>
            <td>{row.projekt_produkt}</td>
            <td>{row.standort}</td>
            <td>{row.haendler}</td>
            <td>{row.datum_letzte_aenderung}</td>
            <td>{row.datum_erstausgabe}</td>
            <td>{row.benutzer_firmcode}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default CustomTable;