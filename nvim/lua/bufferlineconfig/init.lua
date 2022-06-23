require("bufferline").setup{
  --keybinds
  vim.cmd[[
  nnoremap <silent><TAB> :BufferLineCycleNext<CR>
  nnoremap <silent><S-TAB> :BufferLineCyclePrev<CR>
  ]]
}

