import { useNavigate } from "react-router-dom";

export function UsuarioCard({ usuario }) {
  const navigate = useNavigate();

  return (
    <div
      className="bg-zinc-800 p-3 hover:bg-zinc-700 hover:cursor-pointer"
      onClick={() => {
        navigate(`/usuarios/1`);
      }}
    >
      <h1 className="text-white font-bold uppercase rounded-lg">
        prueba tarea
      </h1>
      <p className="text-slate-400">descripcion</p>
    </div>
  );
}