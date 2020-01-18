import React from 'react';
import { Route } from 'react-router-dom';

import OrganisationList from "./containers/organisations/OrganisationListView";
import OrganisationDetail from "./containers/organisations/OrganisationDetailView";
import Login from "./containers/Login";
import Signup from "./containers/Signup";

const BaseRouter = () => (
  <div>
    <Route exact path="/org" component = {OrganisationList} />
    <Route exact path="/org/:organisationID" component={OrganisationDetail} />
    <Route exact path="/login/" component={Login} />
    <Route exact path="/signup/" component={Signup} />
  </div>
);

export default BaseRouter;