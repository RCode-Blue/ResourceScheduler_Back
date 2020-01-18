import React from 'react';
import { Form, Input, Button } from 'antd';

import axios from 'axios';

class OrgCreateUpdateForm extends React.Component {

  handleFormSubmit = (e, type, organisationID) => {
    // e.preventDefault();

    console.log(e.target.elements);

    const orgName = e.target.elements.orgName.value;
    const orgDescription = e.target.elements.orgDesc.value;
    console.log("orgName: " + orgName);
    console.log("orgDescription: " + orgDescription);

    switch(type){
      case 'post':
        // console.log("post");
      return axios.post("http://127.0.0.1:8000/api/org/", {
        name: orgName,
        description: orgDescription
      })
        .then(res => console.log(res))
        .catch(error => console.error(error));

      case 'put':
        // console.log("put");
        return axios.put(`http://127.0.0.1:8000/api/org/${organisationID}/`, {
          name: orgName,
          description: orgDescription
        })
          .then(res => console.log(res))
          .catch(error => console.error(error));

      default:
        return("");
    }

    

  }

  render() {
    return (
      <div>
        <Form onSubmit={(e) =>   this.handleFormSubmit(
          e,
          this.props.requestType,
          this.props.organisationID )}>
          <Form.Item label="Name">
            <Input name="orgName" placeholder="organisation name" />
          </Form.Item>
          <Form.Item label="Description">
            <Input name="orgDesc" placeholder="description of your organisation" />
          </Form.Item>
          <Form.Item>
            <Button type="primary" htmlType="submit">{this.props.btnText}</Button>
          </Form.Item>
        </Form>
      </div>
    );
  }
}

export default OrgCreateUpdateForm;
