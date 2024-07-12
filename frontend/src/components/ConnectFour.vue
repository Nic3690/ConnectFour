<template>
	<div>
		<h1>Connect 4</h1>
		<div v-for="(row, rowIndex) in board" :key="rowIndex" class="row">
			<div
				v-for="(cell, cellIndex) in row"
				:key="cellIndex"
				class="cell"
				@click="makeMove(cellIndex)"
				>
				{{ cell }}
			</div>
		</div>
	</div>
</template>
  
<script>
	export default {
		data() {return {board: [], gameId: 1};},
		created() {this.getBoard();},
		methods: {
			getBoard() {
				fetch(`/api/get_board/${this.gameId}/`)
				.then(response => response.json())
				.then(data => {
					this.board = data.board;
				})
				.catch(error => {
					console.error('Error fetching board:', error);
				});
			},
			makeMove(column) {
				fetch(`/api/make_move/${this.gameId}/`, {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
				},
				body: JSON.stringify({ column: column }),
				})
				.then(response => response.json())
				.then(data => {
					this.board = data.board;
				})
				.catch(error => {
					console.error('Error making move:', error);
				});
			},
		},
	};
</script>
  
<style>
	.row {
		display: flex;
	}
	.cell {
		width: 50px;
		height: 50px;
		border: 1px solid #000;
		display: flex;
		align-items: center;
		justify-content: center;
		cursor: pointer;
	}
</style>