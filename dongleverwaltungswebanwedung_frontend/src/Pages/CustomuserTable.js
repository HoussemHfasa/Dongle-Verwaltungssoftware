import React, { useState, useEffect } from "react";
import { Table, Button, Popconfirm, Form, Select } from "antd";
import { useAuth } from "../Components/AuthContext";
import { Modal } from "antd";
const { Option } = Select;

function CustomuserTable() {
  // Zustandsvariablen
  const [data, setData] = useState([]);
  const [editingId, setEditingId] = useState(null);
  const [form] = Form.useForm();
  const { email, setRole } = useAuth();
  // Daten von der API abrufen
  useEffect(() => {
    fetch("http://127.0.0.1:8000/Adminseite/")
      .then((response) => response.json())
      .then((data) => setData(data.data))
      .catch((error) => console.error(error));
  }, []);
  // Editierbare Zelle-Komponente
  const EditableCell = ({
    editing,
    dataIndex,
    title,
    record,
    index,
    children,
    ...restProps
  }) => {
    const [showConfirm, setShowConfirm] = useState(false);
    // Bestätigungsdialog anzeigen
    const handleConfirm = () => {
      Modal.confirm({
        title: "Bestätigung der Rollenänderung",
        content: `Sind Sie sicher, dass Sie die Rolle in eine ${form.getFieldValue(
          "role"
        )} ändern möchten?`,
        onOk: () => {
          save(record.id);
          setShowConfirm(false);
        },
        onCancel: () => {
          setShowConfirm(false);
        },
        okText: "Ja", // Add this line
        cancelText: "Nein", // Add this line
      });
    };
    // Editierbare Dropdown-Tabelle
    if (editing && dataIndex === "role") {
      return (
        <td {...restProps}>
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
            <Select
              style={{ width: "100%" }}
              value={form.getFieldValue("role")}
              onChange={(value) => {
                form.setFieldsValue({ role: value });

                if (record.email === email) {
                  setRole(value);
                }

                setShowConfirm(true);
              }}
              onBlur={() => setShowConfirm(false)}
            >
              <Option value="Admin">Admin</Option>
              <Option value="Verwalter">Verwalter</Option>
            </Select>
            {showConfirm && (
              <Button type="primary" onClick={handleConfirm}>
                Bestätigen
              </Button>
            )}
          </Form.Item>
        </td>
      );
    }

    return <td {...restProps}>{children}</td>;
  };
  // Löschen eines Benutzers
  const handleDelete = async (record) => {
    if (record.is_superuser === 1) {
      // If the user has is_superuser set to 1, show an alert and return early.
      alert(
        "Sie können ein Admin-Konto mit Superuser-Privilegien nicht löschen."
      );
      return;
    }
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
      title: "Superuser",
      dataIndex: "is_superuser",
      render: (value) => (value === true ? "Ja" : "Nein"),
    },
    {
      title: "Name",
      dataIndex: "name",
    },
    {
      title: "Rolle",
      dataIndex: "role",
      editable: true,
    },
    {
      title: "Firmcode",
      dataIndex: "firm_code",
    },
    {
      title: "Aktionen",
      render: (text, record) => (
        <>
          {record.role !== "Kunde" &&
            !isEditing(record) &&
            record.is_superuser !== 1 && (
              <Button
                type="primary"
                onClick={() => edit(record)}
                style={{ marginRight: 8 }}
              >
                Rolle ändern
              </Button>
            )}
          <Popconfirm
            title={`Sind Sie sicher, dass Sie den Kunden mit der ID ${record.id} löschen möchten?`}
            onConfirm={() => handleDelete(record)}
            okText="Ja"
            cancelText="Nein"
          >
            <Button
              type="danger"
              style={{
                backgroundColor: "red",
                borderColor: "red",
                color: "white",
              }}
            >
              Löschen
            </Button>
          </Popconfirm>
        </>
      ),
    },
  ];
  // Überprüfen, ob eine Zeile bearbeitet wird
  const isEditing = (record) => record.id === editingId;
  // Bearbeitungsmodus aktivieren
  const edit = (record) => {
    form.setFieldsValue({
      role: "",
      ...record,
    });
    setEditingId(record.id);
  };
  // Bearbeitungsmodus abbrechen
  const cancel = () => {
    setEditingId(null);
  };
  // Benutzerdaten speichern
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
  // Bearbeitbare Spalten erstellen
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
      />
    </Form>
  );
}

export default CustomuserTable;
