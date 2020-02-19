import React from 'react';
import { List, Avatar, Icon } from 'antd';
import { blue, grey } from '@ant-design/colors';

const IconText = ({ type, text }) => (
  <span>
    <Icon type={type} style={{ marginRight: 8 }} />
    {text}
  </span>
);


const Bookings = (props) => {
  console.log(props)
  return(
    <List
      itemLayout="vertical"
      size="large"
      pagination={{
        onChange: page => {
          console.log(page);
        },
        pageSize: 3,
      }}
      dataSource={props.data}
      footer={
        <div>
          <b>ant design</b> footer part
        </div>
      }
      renderItem={item => (
        <List.Item
          key={item.id}
          // actions={[
          //   <IconText type="star-o" text="156" key="list-vertical-star-o" />,
          //   <IconText type="like-o" text="156" key="list-vertical-like-o" />,
          //   <IconText type="message" text="2" key="list-vertical-message" />,
          // ]}
          // extra={
          //   <img
          //     width={272}
          //     alt="logo"
          //     src="https://gw.alipayobjects.com/zos/rmsportal/mqaQswcyDLcXyDKnZfES.png"
          //   />
          // }
        >
          <List.Item.Meta
            avatar={
              <Avatar 
            shape="square" 
            size="large" 
            icon="paper-clip" 
            style={{
              // color: grey[1],
              backgroundColor: blue[5]}}
            />
            }
            title={<a href={`/bookings/${item.id}/`}>{item.name}</a>}
            description={item.description}
          />
          {item.content}
        </List.Item>
      )}
    />
  )
}


export default Bookings;