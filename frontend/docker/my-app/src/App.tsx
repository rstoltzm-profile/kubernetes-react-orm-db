import { useState } from 'react';
import Home from './pages/Home';
import Info from './pages/Info';
import About from './pages/About';
import Contact from './pages/Contact';
import './App.css';

function App() {
  const [activeTab, setActiveTab] = useState('Home');

  return (
    <div>
      <header>
        <h1>My React App</h1>
        <nav>
          <button onClick={() => setActiveTab('Home')}>Home</button>
          <button onClick={() => setActiveTab('About')}>About</button>
          <button onClick={() => setActiveTab('Contact')}>Contact</button>
          <button onClick={() => setActiveTab('Info')}>Info</button>
        </nav>
      </header>
      <main>
        {activeTab === 'Home' && <Home />}
        {activeTab === 'About' && <About />}
        {activeTab === 'Contact' && <Contact />}
        {activeTab === 'Info' && <Info />}
      </main>
    </div>
  );
}

export default App;