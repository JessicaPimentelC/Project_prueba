import { useEffect, useState } from "react"
import { ObtenerUsuarios } from "../api/Usuario-api";
import { UsuarioCard } from "./UsuarioCard";

export function Usuario(){
    
    const [usuarios, setUsuario] = useState([]);
    useEffect(() => {

        async function cargarUsuario(){
            const res = await ObtenerUsuarios();
            console.log(res);
            setUsuario(res.data);
        }
        cargarUsuario();
    }, []);
    return(
        <div>
            {usuarios.map((usuario) => (
        <UsuarioCard key='1' usuario={usuario} />
      ))}


        </div>
)
}