import React from 'react';
import { connect } from 'react-redux';

import * as actions from "../../store/actions";

import OrgUsers from "../../components/orgusers/OrgUser";


class OrgUserList extends React.Component {

  componentDidMount(){
    this.props.getOrgUsers();
  }

  render() {
    // console.log(this);
    if(this.props.orgUserList === null){
      return(
        <div>Loading...</div>
      )
    }
    return(
      <OrgUsers data={this.props.orgUserList}/>
    )
  }
}


const mapStateToProps = (state) => {
  return {
    orgUserList: state.orgUserList
  }
}


const mapDispatchToProps = (dispatch) => {
  return {
    getOrgUsers: () => dispatch(actions.getOrgUsers())
  }
}


export default connect(mapStateToProps, mapDispatchToProps)(OrgUserList);