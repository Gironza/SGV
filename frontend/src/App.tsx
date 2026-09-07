import { BrowserRouter, Routes, Route } from "react-router";

import Inicio from "./pages/inicio";
import Login from "./pages/Login";
import Registro from "./pages/Registro";
import Admin from "./pages/Admin";
import Docente from "./pages/Docente";
import Estudiante from "./pages/Estudiante";
import RutaProtegida from "./routes/RutaProtegida";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* INICIO */}
        <Route path="/" element={<Inicio />} />
        {/* LOGIN */}
        <Route path="/login" element={<Login />} />
        {/* REGISTRO */}
        <Route path="/registro" element={<Registro />} />

        {/* ADMINISTRADOR (id_rol=1) */}
        <Route
          path="/admin"
          element={
            <RutaProtegida rolesPermitidos={[1]}>
              <Admin />
            </RutaProtegida>
          }
        />

        {/* DOCENTE (id_rol=2) */}
        <Route
          path="/docente"
          element={
            <RutaProtegida rolesPermitidos={[2]}>
              <Docente />
            </RutaProtegida>
          }
        />

        <Route path="/estudiante" element={<RutaProtegida rolesPermitidos={[3]}><Estudiante /></RutaProtegida>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;