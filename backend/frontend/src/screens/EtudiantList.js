import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Row, Col, Card } from 'react-bootstrap';
import { Link } from 'react-router-dom';

function EtudiantList() {
  const [etudiants, setEtudiants] = useState([]);

  useEffect(() => {
    async function fetchEtudiants() {
      const { data } = await axios.get('http://127.0.0.1:8000/etudiants/api/');
      setEtudiants(data);
    }
    fetchEtudiants();
  }, []);

  return (
    <div>
      <h1>Nos Stagiaires</h1>
      <Row>
        {etudiants.map((etudiant) => (
          <Col key={etudiant.id} sm={12} md={6} lg={4} xl={3}>
            <Card className="my-3 p-3 rounded">
              <Card.Body>
                <Link to={`/etudiants/${etudiant.id}`}>
                  <Card.Title>{etudiant.prenom} {etudiant.nom}</Card.Title>
                </Link>
                <Card.Text>{etudiant.filiere}</Card.Text>
                <Card.Text>{etudiant.annee}</Card.Text>
              </Card.Body>
            </Card>
          </Col>
        ))}
      </Row>
    </div>
  );
}

export default EtudiantList;