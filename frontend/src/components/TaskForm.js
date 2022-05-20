import React from "react";


class TaskForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'name': '',
            'project': '',
            'description': '',
            'created_by': '',
            'project_users': []
        }
    }

    handleChange(event) {
        this.setState(
            {[event.target.name]: event.target.value}
        )
    }
    handleUsersChange(event) {
        if (!event.target.selectedOptions) {
            return
        }
        let users = []
        for (let i=0; i < event.target.selectedOptions.length; i++) {
            users.push(parseInt(event.target.selectedOptions.item(i).value))
        }
        this.setState(
            {"users": users}
        )
    }

    handleOneSelectChange(event) {
        if (!event.target.options[event.target.options.selectedIndex].value) {
            return
        }
        this.setState(
            {[event.target.name]: parseInt(event.target.options[event.target.options.selectedIndex].value)}
        )
    }

    handleSubmit(event) {
        this.props.createTask(
            this.state.name,
            this.state.project,
            this.state.description,
            this.state.created_by,
            this.state.users
        )
        event.preventDefault()
    }

    render() {
        return(
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <input type="text"
                       name="name"
                       placeholder="Название"
                       value={this.state.name}
                       onChange={(event) => this.handleChange(event)}/>
                <select name="project" onChange={(event => this.handleOneSelectChange(event))}>
                    {this.props.projects.map((project) => <option value={project.id}>{project.name}</option>)}
                </select>
                <input type="text"
                   name="description"
                   placeholder="Описание"
                   value={this.state.description}
                   onChange={(event) => this.handleChange(event)}/>
                <select name="created_by" onChange={(event => this.handleOneSelectChange(event))}>
                    {this.props.users.map((user) => <option value={user.id}>{user.username}</option>)}
                </select>
                <select multiple name="users" onChange={(event => this.handleUsersChange(event))}>
                    {this.props.project_users.map((user) => <option value={user.id}>{user.id}</option>)}
                </select>
                <input type="submit" value="Create"/>
            </form>
        )
    }
}

export default TaskForm ;