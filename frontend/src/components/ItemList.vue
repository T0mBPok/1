<template>
  <div>
    <button v-if="!isCreating && !editingItem" @click="startCreating">
      Добавить объект
    </button>

    <ItemForm
      v-if="isCreating"
      @submit="addItem"
      @cancel="cancelCreating"
    />

    <ItemForm
      v-if="editingItem"
      :editableItem="editingItem"
      @submit="updateItem"
      @cancel="cancelEdit"
    />

    <div v-if="!isCreating && !editingItem">
      <ItemView
        v-for="item in items"
        :key="item.id"
        :item="item"
        @delete="deleteItem"
        @edit="startEdit"
      />
    </div>
  </div>
</template>

<script>
import ItemView from './ItemView.vue';
import ItemForm from './ItemForm.vue';
import { fetchItems, createItem, updateItem, deleteItem } from "../api.js";

export default {
  components: { ItemView, ItemForm },
  data() {
    return {
      items: [],
      editingItem: null,
      isCreating: false,  // режим создания
    };
  },
  created() {
    fetchItems()
      .then((res) => {
        this.items = res.data;
      })
      .catch(console.error);
  },
  methods: {
    startCreating() {
      this.isCreating = true;
    },
    cancelCreating() {
      this.isCreating = false;
    },
    addItem(item) {
      createItem(item)
        .then((res) => {
          this.items.push(res.data);
          this.isCreating = false;
        })
        .catch(console.error);
    },
    updateItem(item) {
      updateItem(item)
        .then((res) => {
          this.items = this.items.map((i) => (i.id === item.id ? res.data : i));
          this.editingItem = null;
        })
        .catch(console.error);
    },
    deleteItem(id) {
      deleteItem(id)
        .then(() => {
          this.items = this.items.filter((i) => i.id !== id);
        })
        .catch(console.error)
    },
    startEdit(item) {
      this.editingItem = item;
    },
    cancelEdit() {
      this.editingItem = null;
    },
  },
};
</script>
