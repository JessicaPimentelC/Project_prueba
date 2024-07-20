import { useNavigate } from "react-router-dom";

export function UsuarioCard({ usuario }) {
  const navigate = useNavigate();

  return (
    <div
      className="bg-zinc-800 p-3 hover:bg-zinc-700 hover:cursor-pointer"
      onClick={() => {
        navigate(`/usuario/${usuario.id}`);
      }}
    >
      <h1>{usuario.id}</h1>
      <p>{usuario.username}</p>
    </div>
  );
}