import Header from "./components/Header";
import Footer from "./components/Footer";
import Home from "./screens/Home";
import EtudiantList from "./screens/EtudiantList";
import EtudiantDetail from "./screens/EtudiantDetail";
import { Container } from "react-bootstrap";
import { BrowserRouter, Route, Routes } from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
      <Header />
      <main className="py-5">
        <Container>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/etudiants" element={<EtudiantList />} />
            <Route path="/etudiants/:id" element={<EtudiantDetail />} />
          </Routes>
        </Container>
      </main>
      <Footer />
    </BrowserRouter>
  );
}

export default App;