import { BrowserRouter, Route, Router, Routes } from "react-router-dom"
import { UsuarioPage } from "./pages/UsuarioPage"
import { UsuarioFormPage } from "./pages/UsuarioFormPage"

function App(){
    return (
        <BrowserRouter>
        <Routes>

            <Route path="/usuario" element={<UsuarioPage/>}/>
            <Route path="/usuario-create" element={<UsuarioFormPage/>}/>
        </Routes>
        
        </BrowserRouter>
    )
}
export default App