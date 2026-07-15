import React from 'react';
import { Navbar, Container, Nav } from 'react-bootstrap';
import { LinkContainer } from 'react-router-bootstrap';

function Header() {
  return (
    <header>
      <Navbar bg="dark" variant="dark">
        <Container>
          <LinkContainer to="/">
            <Navbar.Brand>Suivi de Stage</Navbar.Brand>
          </LinkContainer>
          <Nav className="me-auto">
            <LinkContainer to="/">
              <Nav.Link>Accueil</Nav.Link>
            </LinkContainer>
            <LinkContainer to="/etudiants">
              <Nav.Link>Etudiants</Nav.Link>
            </LinkContainer>
          </Nav>
        </Container>
      </Navbar>
    </header>
  )
}

export default Header