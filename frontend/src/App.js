import React from "react";
import axios from "axios";
import UserList from "./components/UserList";


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state ={
            'users': []
        }
    }

    componentDidMount() {
        axios
            .get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                let users = response.data
                this.setState({
                    'users': users
                })
            })
            .catch(error => console.log(error))
    }

    render() {
        return(
            <div>
                <h1>Menu</h1>
                <UserList users={this.state.users}/>
                <h1>Footer</h1>
            </div>
        )
    }
}

export default App;
