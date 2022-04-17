import React from "react";
import axios from "axios";
import Main from "./components/Main";
import UserList from "./components/UserList";
import UserDetail from "./components/UserDetail";
import ProjectUserList from "./components/ProjectUserList";
import ProjectList from "./components/ProjectList";
import ProjectDetail from "./components/ProjectDetail";
import TaskList from "./components/TaskList";
import NotFound from "./components/NotFound";
import {BrowserRouter, Routes, Route, Link} from "react-router-dom";


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state ={
            'users': [],
            'projects': [],
            'project': null,
            'tasks': []
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
        axios
            .get('http://127.0.0.1:8000/api/project-users/')
            .then(response => {
                let project_users = response.data
                this.setState({
                    'project_users': project_users
                })
            })
            .catch(error => console.log(error))
        axios
            .get('http://127.0.0.1:8000/api/projects/')
            .then(response => {
                let projects = response.data
                this.setState({
                    'projects': projects
                })
            })
            .catch(error => console.log(error))
        axios
            .get('http://127.0.0.1:8000/api/tasks/')
            .then(response => {
                let tasks = response.data
                this.setState({
                    'tasks': tasks
                })
            })
            .catch(error => console.log(error))
    }

    render() {
        return(
            <div>
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li><Link to='/'>Главная</Link></li>
                            <li><Link to='/users'>Пользователи</Link></li>
                            <li><Link to='/projects'>Проекты</Link></li>
                            <li><Link to='/project-users'>Пользователи проектов</Link></li>
                            <li><Link to='/tasks'>Задачи</Link></li>
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
                        <Route exact path='*' element={<NotFound/>}/>
                    </Routes>
                </BrowserRouter>
                <h1>Footer</h1>
            </div>
        )
    }
}

export default App;
