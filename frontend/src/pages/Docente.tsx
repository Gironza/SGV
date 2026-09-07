import { useNavigate } from "react-router";
import { useAuth } from "../context/AuthContext";
import "bootstrap/dist/css/bootstrap.min.css";
import "../styles/styles.css";

function Docente() {
  const { logout } = useAuth();
  const navigate = useNavigate();
  function handleLogout() {
    logout();
    navigate("/");
  }
  return (
    <div className="container mt-4">
      {/* CERRAR SESIÓN */}
      <div className="mb-4">
        <button onClick={handleLogout} className="logout-btn border-0 bg-transparent">
          <i className="fa-solid fa-right-from-bracket"></i> Cerrar sesión
        </button>
      </div>
      <h1 className="mb-4">
        Panel Docente
      </h1>
      {/* TARJETAS */}
      <div className="row">
        <div className="col-md-4 mb-4">
          <div className="card p-3">
            <h3>3</h3>
            <p>
              Votaciones creadas
            </p>
          </div>
        </div>
        <div className="col-md-4 mb-4">
          <div className="card p-3">
            <h3>250</h3>
            <p>
              Estudiantes registrados
            </p>
          </div>
        </div>
        <div className="col-md-4 mb-4">
          <div className="card p-3">
            <h3>90%</h3>
            <p>
              Participación estudiantil
            </p>
          </div>
        </div>
      </div>
      {/* CARGA MASIVA */}
      <div className="card p-4 mt-2">
        <h3 className="mb-2">
          Cargar estudiantes
        </h3>
        <p>
          Puedes cargar varios estudiantes al mismo
          tiempo utilizando un archivo.
        </p>
        <div className="mb-3">
          <label className="form-label">
            Seleccionar archivo
          </label>
          <input
            type="file"
            className="form-control"
            accept=".csv,.xlsx,.xls"
          />
        </div>
        <button className="btn btn-primary">
          Cargar estudiantes
        </button>
      </div>
      {/* TABLA */}
      <div className="card p-4 mt-4">
        <h3 className="mb-3">
          Votaciones creadas
        </h3>
        <table className="table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Votación</th>
              <th>Curso</th>
              <th>Estado</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>01</td>
              <td>Personero 2026</td>
              <td>11A</td>
              <td>Activa</td>
            </tr>
            <tr>
              <td>02</td>
              <td>Contralor 2026</td>
              <td>10B</td>
              <td>Finalizada</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Docente;