<template>
  <form @submit.prevent="submitForm">
    <div>
      <label>Kind:</label>
      <input type="text" v-model="localItem.kind" required />
    </div>
    <div>
      <label>Name:</label>
      <input type="text" v-model="localItem.name" required />
    </div>
    <div>
      <label>Age:</label>
      <input type="text" v-model.number="localItem.age" required min="0" />
    </div>
    <button type="submit">
      {{ localItem.id ? 'Сохранить' : 'Добавить' }}
    </button>
    <button type="button" @click="$emit('cancel')">Отмена</button>
  </form>
</template>

<script>
export default {
  props: {
    editableItem: Object,
  },
  data() {
    return {
      localItem: this.editableItem
        ? { ...this.editableItem }
        : { kind: '', name: '', age: null },
    };
  },
  watch: {
    editableItem(newVal) {
      this.localItem = newVal ? { ...newVal } : { kind: '', name: '', age: null };
    },
  },
  methods: {
    submitForm() {
      this.$emit('submit', this.localItem);
    },
  },
};
</script>
