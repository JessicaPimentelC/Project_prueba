import './App.css';

import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Register from './components/Register';
import Login from './components/Login';
import { UsuarioPage } from "./pages/UsuarioPage"
import { UsuarioFormPage } from "./pages/UsuarioFormPage"
import { Navigation } from './components/Navigation';
import { LoginFormPage } from './pages/LoginFormPage';


const App = () => {
  return (
    <Router>
      <div>
      <Navigation/>
        <Routes>
          
          <Route path="/" element={<Navigate to="/login"/>}/>
          <Route path="/register" element={<Register/>}/>
          <Route path="/login" element={<LoginFormPage/>} />
          <Route path="/usuario" element={<UsuarioPage/>}/>
          <Route path="/usuario-create" element={<UsuarioFormPage/>}/>
          <Route path="/usuario/:id" element={<UsuarioFormPage/>}/>

        </Routes>
      </div>
    </Router>
  );
};

export default App;
