import React from 'react';
import { List, Avatar } from 'antd';

// const IconText = ({ type, text }) => (
//   <span>
//     <Icon type={type} style={{ marginRight: 8 }} />
//     {text}
//   </span>
// );

const Users = (props) => {
  return(
    <List
    itemLayout="horizontal"
    pagination={{
      onChange: page => {
        // console.log(page);
      },
      pageSize: 3,
    }}
    dataSource={props.data}
    renderItem={item => (
      <List.Item
        key={item.username}

      >
        <List.Item.Meta
          avatar={<Avatar src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png" />}
          title={<a href={`/users/${item.id}/`}>{item.username}</a>}
          description={`${item.job_title}`}
          
        />
        {item.content}
      </List.Item>
    )}
  />
  )
}

export default Users;