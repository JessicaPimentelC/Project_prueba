import { useEffect, useState } from "react"
import { obtenerUsuarios } from "../api/Usuario-api";
import { UsuarioCard } from "./UsuarioCard";

export function Usuario(){
    
    const [usuarios, setUsuario] = useState([]);
    useEffect(() => {

        async function cargarUsuario(){
            const res = await obtenerUsuarios();
            console.log(res);
            setUsuario(res.data);
        }
        cargarUsuario();
    }, []);
    return(
        <div>
            {usuarios.map((usuario) => (
        <UsuarioCard key={usuario.id} usuario={usuario} />
    ))}


        </div>
)
}