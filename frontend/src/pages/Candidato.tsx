import { Link } from "react-router";
import "bootstrap/dist/css/bootstrap.min.css";
import "@fortawesome/fontawesome-free/css/all.min.css";
import "../styles/styles.css";

function Candidato() {
  return (
    <div className="dashboard">
      {/* SIDEBAR */}
      <div className="sidebar">
        <h2>
          SGV
        </h2>
        <ul>
          <li className="active">
            <i className="fa-solid fa-user"></i>
            Mi campaña
          </li>
          <li>
            <i className="fa-solid fa-bullhorn"></i>
            Propuestas
          </li>
          <li>
            <i className="fa-solid fa-chart-column"></i>
            Resultados
          </li>
          <li>
            <Link
              to="/"
              className="logout-btn"
            >
              <i className="fa-solid fa-right-from-bracket"></i>
              Cerrar sesión
            </Link>
          </li>
        </ul>
      </div>
      {/* CONTENIDO */}
      <div className="main-content">
        <div className="topbar">
          <div>
            <h1>
              Panel Candidato
            </h1>
            <p>
              Administra tu campaña electoral
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Candidato;