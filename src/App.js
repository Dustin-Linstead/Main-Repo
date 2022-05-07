import './App.css';
import { Router } from '@reach/router';
import Header from './components/Header';
import Main from './views/Main';
import Edit from './views/Edit';
import New from './views/New';
import Single from './views/Single';
function App() {
  return (
    <div className="App">
      <Header/>
      <Router>
      <Main path= "/pets"/>
      <Single path="/pets/:id"/>
      <Edit path="/pets/:id/edit"/>
      <New path="/pets/new"/>
      </Router>
    </div>
  );
}

export default App;
