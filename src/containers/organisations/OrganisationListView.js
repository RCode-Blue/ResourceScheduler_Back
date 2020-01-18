import React from 'react';
import axios from 'axios';

import Organisations from "../../components/organisations/Organisation";
import OrgCreateUpdateForm from "../../components/organisations/OrganisationCreateUpdate";


class OrganisationList extends React.Component {
  
  state = {
    articles: []
  }

  componentDidMount() {
    // axios.get("http://127.0.0.1:8000/api/org/")
    axios.get("/api/org/")
      .then(res => {
        this.setState({
          organisations: res.data
        });
        // console.log(res);
      })
  }

  render() {
    return (
      <div>
        <Organisations data={this.state.organisations}/>
        <br />
        <h2>Create new organisation</h2>
        <OrgCreateUpdateForm 
          requestType="post"
          organisationID={null}
          btnText="Create"/>
      </div>
    );
  }
}

export default OrganisationList;