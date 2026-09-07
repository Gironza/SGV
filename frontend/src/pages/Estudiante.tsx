import { useEffect, useState } from "react";
import { useAuth } from "../context/AuthContext";
import eleccionService, { type EleccionOut } from "../services/eleccion.service";
import votoService, { type CandidatoVotacionOut } from "../services/voto.service";
import resultadoService, { type ResultadoEleccionOut } from "../services/resultado.service";
import candidatoService from "../services/candidato.service";


function Estudiante() {
  const { usuario, logout } = useAuth();
  const [elecciones, setElecciones] = useState<EleccionOut[]>([]);
  const [seleccion, setSeleccion] = useState<EleccionOut | null>(null);
  const [candidatos, setCandidatos] = useState<CandidatoVotacionOut[]>([]);
  const [yaVoto, setYaVoto] = useState(false);
  const [resultado, setResultado] = useState<ResultadoEleccionOut | null>(null);
  const [mensaje, setMensaje] = useState("");

  useEffect(() => { eleccionService.listar().then(setElecciones); }, []);

  async function abrirEleccion(e: EleccionOut) {
    setSeleccion(e); setResultado(null); setMensaje("");
    const estado = await votoService.estado(e.id_eleccion);
    setYaVoto(estado.ya_voto);
    if (estado.ya_voto) {
      resultadoService.obtener(e.id_eleccion).then(setResultado);
    } else {
      votoService.candidatos(e.id_eleccion).then(setCandidatos);
    }
  }

  async function votar(idCandidato: number | null) {
    if (!seleccion) return;
    try {
      const r = await votoService.votar(seleccion.id_eleccion, idCandidato);
      setMensaje(`Voto registrado. Certificado: ${r.codigo_certificado}`);
      setYaVoto(true);
      resultadoService.obtener(seleccion.id_eleccion).then(setResultado);
    } catch (err: any) {
      setMensaje(err.response?.data?.detail || "Error al votar");
    }
  }

  const [misCandidaturas, setMisCandidaturas] = useState<Record<number, number>>({});
// clave: id_eleccion, valor: id_candidato

    async function postularme(idEleccion: number) {
    const r: any = await candidatoService.inscribir(idEleccion);
    setMisCandidaturas(prev => ({ ...prev, [idEleccion]: r.id_candidato }));
    }

    async function retirarCandidatura(idEleccion: number) {
    const idCandidato = misCandidaturas[idEleccion];
    try {
        await candidatoService.retirar(idCandidato);
        setMisCandidaturas(prev => {
        const copia = { ...prev };
        delete copia[idEleccion];
        return copia;
        });
    } catch (err: any) {
        alert(err.response?.data?.detail || "No se pudo retirar (¿ya tiene votos?)");
    }
    }
  return (
    <div className="container mt-4">
      <div className="d-flex justify-content-between mb-4">
        <h1>Panel Estudiante — {usuario?.nombre}</h1>
        <button className="btn btn-danger" onClick={logout}>Cerrar sesión</button>
      </div>

      {!seleccion && (
        <div className="row">
          {elecciones.map((e) => (
            <div className="col-md-4 mb-3" key={e.id_eleccion}>
              <div className="card p-3">
                <h5>{e.titulo}</h5>
                <p>{e.nombre_estado}</p>
                <button className="btn btn-primary" onClick={() => abrirEleccion(e)}>Ver</button>
                {misCandidaturas[e.id_eleccion] ? (
                <button className="btn btn-outline-danger ms-2" onClick={() => retirarCandidatura(e.id_eleccion)}>
                    Retirar candidatura
                </button>
                ) : (
                <button className="btn btn-outline-success ms-2" onClick={() => postularme(e.id_eleccion)}>
                    Postularme
                </button>
                )}
              </div>
            </div>
          ))}
        </div>
      )}

      {seleccion && (
        <div>
          <button className="btn btn-secondary mb-3" onClick={() => setSeleccion(null)}>← Volver</button>
          <h3>{seleccion.titulo}</h3>
          {mensaje && <div className="alert alert-info">{mensaje}</div>}

          {!yaVoto && (
            <div className="row">
              {candidatos.map((c) => (
                <div className="col-md-4 mb-3" key={c.id_candidato}>
                  <div className="card p-3">
                    <h5>{c.nombre} {c.apellido}</h5>
                    <p>{c.propuesta}</p>
                    <button className="btn btn-success" onClick={() => votar(c.id_candidato)}>Votar</button>
                  </div>
                </div>
              ))}
              <div className="col-md-4 mb-3">
                <div className="card p-3">
                  <h5>Voto en blanco</h5>
                  <button className="btn btn-outline-secondary" onClick={() => votar(null)}>Votar en blanco</button>
                </div>
              </div>
            </div>
          )}

          {yaVoto && resultado && (
            <div>
              <h4>Resultados ({resultado.nombre_estado})</h4>
              <table className="table">
                <thead><tr><th>Candidato</th><th>Votos</th></tr></thead>
                <tbody>
                  {resultado.candidatos.map((c) => (
                    <tr key={c.id_candidato}><td>{c.nombre} {c.apellido}</td><td>{c.total_votos}</td></tr>
                  ))}
                  <tr><td>Blancos</td><td>{resultado.votos_blancos}</td></tr>
                </tbody>
              </table>
              {resultado.ganador && <p><b>Ganador:</b> {resultado.ganador}</p>}
            </div>
          )}
        </div>
      )}
    </div>
  );
}
export default Estudiante;