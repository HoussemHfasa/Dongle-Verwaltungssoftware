import React, { useState, useEffect } from "react";
import { Table, Button, Popconfirm, Form, Input, Select } from "antd";
import { useAuth } from "../Components/AuthContext";

const { Option } = Select;

function CustomuserTable() {
  const [data, setData] = useState([]);
  const [editingId, setEditingId] = useState(null);
  const [form] = Form.useForm();
  const { email, setRole } = useAuth();

  useEffect(() => {
    fetch("http://127.0.0.1:8000/Adminseite/")
      .then((response) => response.json())
      .then((data) => setData(data.data))
      .catch((error) => console.error(error));
  }, []);

  const EditableCell = ({
    editing,
    dataIndex,
    title,
    record,
    index,
    children,
    ...restProps
  }) => {
    const shouldRenderDropdown =
      record && ["Admin", "Verwalter"].includes(record[dataIndex]);
    const inputNode =
      dataIndex === "role" ? (
        shouldRenderDropdown ? (
          <Select
            style={{ width: "100%" }}
            value={form.getFieldValue("role")}
            onChange={(value) => form.setFieldsValue({ role: value })}
            onBlur={() => save(record.id)}
          >
            <Option value="Admin">Admin</Option>
            <Option value="Verwalter">Verwalter</Option>
          </Select>
        ) : (
          record[dataIndex]
        )
      ) : (
        dataIndex !== "role" && <Input />
      );

    return (
      <td {...restProps}>
        {editing ? (
          <Form.Item
            name={dataIndex}
            style={{ margin: 0 }}
            rules={[
              {
                required: true,
                message: `Please Input ${title}!`,
              },
            ]}
          >
            {inputNode}
          </Form.Item>
        ) : (
          children
        )}
      </td>
    );
  };

  const handleDelete = async (record) => {
    try {
      const response = await fetch(
        `http://127.0.0.1:8000/Adminseite/${record.id}/`,
        {
          method: "DELETE",
        }
      );

      if (response.ok) {
        setData(data.filter((item) => item.id !== record.id));
      } else {
        console.error(`Failed to delete Customuser with id ${record.id}`);
      }
    } catch (error) {
      console.error(error);
    }
  };

  const columns = [
    {
      title: "ID",
      dataIndex: "id",
    },
    {
      title: "Email",
      dataIndex: "email",
    },
    {
      title: "Name",
      dataIndex: "name",
    },
    {
      title: "Role",
      dataIndex: "role",
      editable: true,
    },
    {
      title: "Firm Code",
      dataIndex: "firm_code",
    },
    {
      title: "Delete",
      render: (text, record) => (
        <Popconfirm
          title={`Are you sure you want to delete the Customuser with id ${record.id}?`}
          onConfirm={() => handleDelete(record)}
          okText="Yes"
          cancelText="No"
        >
          <Button type="danger">Delete</Button>
        </Popconfirm>
      ),
    },
  ];

  const isEditing = (record) => record.id === editingId;

  const edit = (record) => {
    form.setFieldsValue({
      role: "",
      ...record,
    });
    setEditingId(record.id);
  };

  const cancel = () => {
    setEditingId(null);
  };

  const save = async (id) => {
    try {
      const row = await form.validateFields();
      const newData = [...data];
      const index = newData.findIndex((item) => id === item.id);

      if (index > -1) {
        const updatedItem = { ...newData[index], ...row };
        try {
          const response = await fetch(
            `http://127.0.0.1:8000/Adminseite/${id}/`,
            {
              method: "PUT",
              headers: {
                "Content-Type": "application/json",
              },
              body: JSON.stringify(updatedItem),
            }
          );

          if (response.ok) {
            newData.splice(index, 1, updatedItem);
            setData(newData);
            setEditingId(null);
            if (updatedItem.email === email) {
              setRole(updatedItem.role);
            }
          } else {
            console.error(`Failed to update Customuser with id ${id}`);
          }
        } catch (error) {
          console.error(`Failed to update Customuser with id ${id}`, error);
        }
      } else {
        newData.push(row);
        setData(newData);
        setEditingId(null);
      }
    } catch (errInfo) {
      console.log("Validate Failed:", errInfo);
    }
  };

  const columnsWithEdit = columns.map((col) => {
    if (!col.editable) {
      return col;
    }
    return {
      ...col,
      onCell: (record) => ({
        record,
        dataIndex: col.dataIndex,
        title: col.title,
        editing: isEditing(record),
      }),
    };
  });

  return (
    <Form form={form} component={false}>
      <Table
        components={{
          body: {
            cell: EditableCell,
          },
        }}
        dataSource={data}
        columns={columnsWithEdit}
        rowClassName="editable-row"
        pagination={{
          onChange: cancel,
        }}
        rowKey="id"
        onRow={(record) => ({
          onClick: () => {
            if (!isEditing(record)) {
              edit(record);
            }
          },
        })}
      />
    </Form>
  );
}

export default CustomuserTable;
