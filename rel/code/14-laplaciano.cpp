Mat LaplacianPyramid::Reconstruct() const {
  Mat base = pyramid_.back();
  Mat expanded;

  for (int i = pyramid_.size() - 2; i >= 0; i--) {
    vector<int> subwindow;
    GaussianPyramid::GetLevelSize(subwindow_, i, &subwindow);
    int row_offset = ((subwindow[0] % 2) == 0) ? 0 : 1;
    int col_offset = ((subwindow[2] % 2) == 0) ? 0 : 1;

    expanded.create(pyramid_[i].rows, pyramid_[i].cols, base.type());

    if (base.channels() == 1) {
      GaussianPyramid::Expand<double>(base, row_offset, col_offset, expanded);
    } else if (base.channels() == 3) {
      GaussianPyramid::Expand<Vec3d>(base, row_offset, col_offset, expanded);
    }
    base = expanded + pyramid_[i];
  }

  return base;
}