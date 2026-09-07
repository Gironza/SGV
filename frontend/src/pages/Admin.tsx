import { useEffect, useState } from "react";
import { useNavigate } from "react-router";
import { useAuth } from "../context/AuthContext";
import eleccionService, { type EleccionOut } from "../services/eleccion.service";
import "bootstrap/dist/css/bootstrap.min.css";
import "@fortawesome/fontawesome-free/css/all.min.css";
import "../styles/styles.css";

function Admin() {
  const [elecciones, setElecciones] = useState<EleccionOut[]>([]);
  useEffect(() => {
    eleccionService.listar().then(setElecciones).catch(() => {});
  }, []);
  const { logout } = useAuth();
  const navigate = useNavigate();
  function handleLogout() {
    logout();
    navigate("/");
  }
  const [titulo, setTitulo] = useState("");
  const [fechaInicio, setFechaInicio] = useState("");
  const [fechaFin, setFechaFin] = useState("");

  async function crearEleccion(e: React.FormEvent) {
    e.preventDefault();
    await eleccionService.crear({ titulo, fecha_inicio: fechaInicio, fecha_fin: fechaFin });
    setTitulo(""); setFechaInicio(""); setFechaFin("");
    eleccionService.listar().then(setElecciones);
  }
  return (
    <div className="dashboard">
      {/* SIDEBAR */}
      <div className="sidebar">
        <h2>SGV</h2>
        <ul>
          <li className="active">
            <i className="fa-solid fa-chart-line"></i>
            Dashboard
          </li>
          <li>
            <i className="fa-solid fa-users"></i>
            Usuarios
          </li>
          <li>
            <i className="fa-solid fa-box-ballot"></i>
            Votaciones
          </li>
          <li>
            <i className="fa-solid fa-chart-pie"></i>
            Resultados
          </li>
          <li>
            <i className="fa-solid fa-gear"></i>
            Configuración
          </li>
          <li>
            <button onClick={handleLogout} className="logout-btn border-0 bg-transparent">
              <i className="fa-solid fa-right-from-bracket"></i> Cerrar sesión
            </button>
          </li>
        </ul>
      </div>
      {/* MAIN */}
      <div className="main-content">
        <div className="topbar">
          <div>
            <h1>
              Panel Administrador
            </h1>
            <p>
              Bienvenido al sistema EduVota
            </p>
          </div>
          <div className="profile">
            <img
              src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
              alt="Administrador"
            />
            <div>
              <h5>
                Administrador
              </h5>
              <small>
                admin@SGV.com
              </small>
            </div>
          </div>
        </div>
        {/* CARDS */}
        <div className="row mt-4">
          <div className="col-md-3 mb-4">
            <div className="dashboard-card">
              <i className="fa-solid fa-users"></i>
              <div>
                <h3>1,240</h3>
                <p>Usuarios</p>
              </div>
            </div>
          </div>
          <div className="col-md-3 mb-4">
            <div className="dashboard-card">
              <i className="fa-solid fa-box-ballot"></i>
              <div>
                <h3>12</h3>
                <p>Votaciones</p>
              </div>
            </div>
          </div>
          <div className="col-md-3 mb-4">
            <div className="dashboard-card">
              <i className="fa-solid fa-chart-column"></i>
              <div>
                <h3>89%</h3>
                <p>Participación</p>
              </div>
            </div>
          </div>
          <div className="col-md-3 mb-4">
            <div className="dashboard-card">
              <i className="fa-solid fa-check"></i>
              <div>
                <h3>560</h3>
                <p>Votos</p>
              </div>
            </div>
          </div>
        </div>
        {/* GRÁFICOS */}
        <div className="row">
          <div className="col-md-8 mb-4">
            <div className="chart-box">
              <h4>
                Participación semanal
              </h4>
              <img
                src="https://quickchart.io/chart?c={type:'bar',data:{labels:['Lun','Mar','Mie','Jue','Vie'],datasets:[{label:'Votos',data:[12,19,8,15,20]}]}}"
                className="img-fluid"
                alt="Participación semanal"
              />
            </div>
          </div>
          <div className="col-md-4 mb-4">
            <div className="chart-box">
              <h4>
                Roles
              </h4>
              <img
                src="https://quickchart.io/chart?c={type:'doughnut',data:{labels:['Admin','Docente','Estudiante'],datasets:[{data:[10,30,60]}]}}"
                className="img-fluid"
                alt="Roles"
              />
            </div>
          </div>
        </div>
        <form onSubmit={crearEleccion} className="card p-3 mb-4">
          <h4>Crear elección</h4>
          <input className="form-control mb-2" placeholder="Título" value={titulo} onChange={e=>setTitulo(e.target.value)} required />
          <input type="datetime-local" className="form-control mb-2" value={fechaInicio} onChange={e=>setFechaInicio(e.target.value)} required />
          <input type="datetime-local" className="form-control mb-2" value={fechaFin} onChange={e=>setFechaFin(e.target.value)} required />
          <button className="btn btn-primary">Crear</button>
        </form>
        {/* TABLA */}
        <div className="table-box">
          <h4>Elecciones</h4>
          <table className="table">
            <thead>
              <tr><th>ID</th><th>Título</th><th>Estado</th><th>Fin</th></tr>
            </thead>
            <tbody>
              {elecciones.map((e) => (
                <tr key={e.id_eleccion}>
                  <td>{e.id_eleccion}</td>
                  <td>{e.titulo}</td>
                  <td>{e.nombre_estado}</td>
                  <td>{new Date(e.fecha_fin).toLocaleDateString()}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
  
};

export default Admin;