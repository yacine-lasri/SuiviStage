import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Row, Col, ListGroup, Button } from 'react-bootstrap';
import { Link, useParams } from 'react-router-dom';

function EtudiantDetail() {
  const [etudiant, setEtudiant] = useState([]);
  const { id } = useParams();

  useEffect(() => {
    async function fetchEtudiant() {
      const { data } = await axios.get(`http://127.0.0.1:8000/etudiants/api/${id}/`);
      setEtudiant(data);
    }
    fetchEtudiant();
  }, [id]);

  return (
    <div>
      <Link to="/etudiants" className="btn btn-light my-3">
        Retour
      </Link>
      <Row>
        <Col md={6}>
          <ListGroup variant="flush">
            <ListGroup.Item>
              <h3>{etudiant.prenom} {etudiant.nom}</h3>
            </ListGroup.Item>
            <ListGroup.Item>
              Email: {etudiant.email}
            </ListGroup.Item>
            <ListGroup.Item>
              Filière: {etudiant.filiere}
            </ListGroup.Item>
            <ListGroup.Item>
              Année: {etudiant.annee}
            </ListGroup.Item>
            <ListGroup.Item>
              Téléphone: {etudiant.telephone}
            </ListGroup.Item>
          </ListGroup>
        </Col>
      </Row>
    </div>
  );
}

export default EtudiantDetail;