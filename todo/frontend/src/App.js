import './App.css';
import React from "react";
import UserList from "./components/Users";
import axios from "axios";
import Footer from "./components/Footer";
import Header from "./components/Header";

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            users: []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users/').then(
            response => {
                const users = response.data
                this.setState({'users': users})
            }).catch(error => console.log(error))

    }

    render() {
        return (
            <div className="App Site">
                <div className="App-header">
                    <Header/>
                </div>
                <body>
                <div className="main">
                    <UserList users={this.state.users}/>
                </div>
                <div className="App-footer">
                    <Footer/>
                </div>
                </body>
            </div>
        )
    }
}

export default App;
