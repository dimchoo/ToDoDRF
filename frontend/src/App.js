import React from "react";
import axios from "axios";
import Main from "./components/Main";
import UserList from "./components/UserList";
import UserDetail from "./components/UserDetail";
import ProjectUserList from "./components/ProjectUserList";
import ProjectList from "./components/ProjectList";
import ProjectDetail from "./components/ProjectDetail";
import TaskList from "./components/TaskList";
import LoginForm from "./components/LoginForm";
import NotFound from "./components/NotFound";
import {BrowserRouter, Routes, Route, Link} from "react-router-dom";


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state ={
            'users': [],
            'project_users': [],
            'projects': [],
            'project': null,
            'tasks': [],
            'token': ''
        }
    }

    obtainAuthToken(login, password) {
        axios
            .post('http://127.0.0.1:8000/api-auth-token/', {"username": login, "password": password})
            .then(response => {
                let token = response.data.token
                console.log(token)
                localStorage.setItem('token', token)
                this.setState({
                    'token': token
                }, this.getData)
            })
            .catch(error => console.log(error))

    }

    componentDidMount() {
        let token =  localStorage.getItem('token')
        this.setState({
            'token': token
        }, this.getData)
    }

    logOut() {
        localStorage.setItem('token', '')
        this.setState({
            'token': ''
        }, this.getData)
    }

    isAuth() {
        return !!this.state.token
    }

    getHeaders() {
        if (this.isAuth()) {
            return {'Authorization': 'Token ' + this.state.token}
        }
        return {}
    }

    getData() {
        let headers = this.getHeaders()
        axios
            .get('http://127.0.0.1:8000/api/users/', {headers})
            .then(response => {
                let users = response.data
                this.setState({
                    'users': users
                })
            })
            .catch(
                error => {
                    this.setState({
                        'users': []
                    })
                    console.log(error)
                }
            )
        axios
            .get('http://127.0.0.1:8000/api/project-users/', {headers})
            .then(response => {
                let project_users = response.data
                this.setState({
                    'project_users': project_users
                })
            })
            .catch(
                error => {
                    this.setState({
                        'project_users': []
                    })
                    console.log(error)
                }
            )
        axios
            .get('http://127.0.0.1:8000/api/projects/', {headers})
            .then(response => {
                let projects = response.data
                this.setState({
                    'projects': projects
                })
            })
            .catch(
                error => {
                    this.setState({
                        'projects': []
                    })
                    console.log(error)
                }
            )
        axios
            .get('http://127.0.0.1:8000/api/tasks/', {headers})
            .then(response => {
                let tasks = response.data
                this.setState({
                    'tasks': tasks
                })
            })
            .catch(
                error => {
                    this.setState({
                        'tasks': []
                    })
                    console.log(error)
                }
            )
    }

    render() {
        return(
            <div>
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li><Link to='/'>??????????????</Link></li>
                            <li><Link to='/users'>????????????????????????</Link></li>
                            <li><Link to='/projects'>??????????????</Link></li>
                            <li><Link to='/project-users'>???????????????????????? ????????????????</Link></li>
                            <li><Link to='/tasks'>????????????</Link></li>
                            <li>
                                { this.isAuth() ? <button onClick={() => this.logOut()}>Logout</button> : <Link to='/login'>Login</Link> }
                            </li>
                        </ul>
                    </nav>
                    <Routes>
                        <Route exact path='/' element={<Main/>}/>
                        <Route exact path='/users' element={<UserList users={this.state.users}/>}/>
                        <Route exact path='/project-users' element={<ProjectUserList project_users={this.state.project_users}/>}/>
                        <Route exact path='/user/:id' element={<UserDetail users={this.state.users}/>}/>
                        <Route exact path='/projects' element={<ProjectList projects={this.state.projects}/>}/>
                        <Route exact path='/project/:id' element={<ProjectDetail projects={this.state.projects}/>}/>
                        <Route exact path='/tasks' element={<TaskList tasks={this.state.tasks}/>}/>
                        <Route exact path='/login' element={
                            <LoginForm obtainAuthToken={(login, password) => this.obtainAuthToken(login, password)}/>}/>
                        <Route exact path='*' element={<NotFound/>}/>
                    </Routes>
                </BrowserRouter>
                <h1>Footer</h1>
            </div>
        )
    }
}

export default App;
