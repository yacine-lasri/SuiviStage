import React from 'react';
import { Alert, Button } from 'react-bootstrap';

function Home() {
  return (
    <Alert variant="primary" className="rounded">
      <h1>Bienvenue sur Suivi de Stage</h1>
      <p>Gérez vos stagiaires, entreprises, rapports et évaluations.</p>
      <p>
        <Button variant="primary">Voir les étudiants</Button>
      </p>
    </Alert>
  );
}

export default Home;