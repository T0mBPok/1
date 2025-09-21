<template>
  <div class="item-view">
    <p><strong>Kind:</strong> {{ item.kind }}</p>
    <p><strong>Name:</strong> {{ item.name }}</p>
    <p><strong>Age:</strong> {{ item.age }}</p>
    <button @click="$emit('edit', item)">Редактировать</button>
    <button @click="$emit('delete', item.id)">Удалить</button>
  </div>
</template>

<script>
export default {
  props: ['item'],
};
</script>
