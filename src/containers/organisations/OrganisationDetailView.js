import React from 'react';
import axios from 'axios';

import { Card, Button } from 'antd';

import OrgCreateUpdateForm from "../../components/organisations/OrganisationCreateUpdate";

class OrganisationDetail extends React.Component {

  state = {
    organisation: {}
  }

  componentDidMount() {
    // console.log(this);
    const organisationID = this.props.match.params.organisationID;
    // axios.get(`http://127.0.0.1:8000/api/org/${organisationID}/`)
    axios.get(`/api/org/${organisationID}/`)
      .then(res => {
        this.setState({
          organisation: res.data
        });
        // console.log(res.data);
      })
  }

  handleDelete = (e) => {
    const organisationID = this.props.match.params.organisationID;
    axios.delete(`http://127.0.0.1:8000/api/org/${organisationID}/`)
      // .then(res => console.log(res))
      // .catch(error => console.error(error));
    // this.props.history.push("/org");
  }

  render() {
    // console.log(this);
    return (
      <div>
        <Card title={this.state.organisation.name}>
          <p>{this.state.organisation.description}</p>
        </Card><br />
        <h2>Edit Organisation</h2>
        <OrgCreateUpdateForm 
          requestType="put"
          organisationID={this.props.match.params.organisationID}
          btnText="Update" />
          <form onSubmit={this.handleDelete}>
            <Button type="danger" htmlType="submit">Delete</Button>
          </form>
      </div>
    )
  }
}

export default OrganisationDetail;