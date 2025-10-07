function showToast(title, message, type = 'normal', duration = 3000) {
  const toast = document.getElementById('toast-component');
  const toastTitle = document.getElementById('toast-title');
  const toastMessage = document.getElementById('toast-message');
  const toastIcon = document.getElementById('toast-icon');

  if (!toast) return;

  // Reset style & transition
  toast.style.border = 'none';
  toast.classList.remove(
    'bg-red-50', 'border-red-500', 'text-red-600',
    'bg-green-50', 'border-green-500', 'text-green-600',
    'bg-white', 'border-gray-300', 'text-gray-800',
    'shadow-lg', 'shadow-green-200', 'shadow-red-200'
  );

  // Default icon
  let icon = '💬';

  // Type-based styling
  if (type === 'success') {
    toast.classList.add('bg-green-50', 'border-green-500', 'text-green-700', 'shadow-green-200');
    toast.style.border = '1px solid #22c55e';
    icon = '✅';
  } else if (type === 'error') {
    toast.classList.add('bg-red-50', 'border-red-500', 'text-red-700', 'shadow-red-200');
    toast.style.border = '1px solid #ef4444';
    icon = '❌';
  } else if (type === 'warning') {
    toast.classList.add('bg-yellow-50', 'border-yellow-400', 'text-yellow-700', 'shadow-yellow-200');
    toast.style.border = '1px solid #facc15';
    icon = '⚠️';
  } else {
    toast.classList.add('bg-white', 'border-gray-300', 'text-gray-800', 'shadow-lg');
    toast.style.border = '1px solid #d1d5db';
  }

  // Update content
  toastTitle.textContent = title;
  toastMessage.textContent = message;
  toastIcon.textContent = icon;

  // Animate In
  toast.classList.remove('opacity-0', 'translate-y-8', 'scale-90');
  toast.classList.add('opacity-100', 'translate-y-0', 'scale-100');

  // Clear previous timeout if any
  if (toast.hideTimeout) clearTimeout(toast.hideTimeout);

  // Animate Out after duration
  toast.hideTimeout = setTimeout(() => {
    toast.classList.remove('opacity-100', 'translate-y-0', 'scale-100');
    toast.classList.add('opacity-0', 'translate-y-8', 'scale-90');
  }, duration);
}

// Optional: manual close button (if ada tombol close di HTML)
const closeBtn = document.getElementById('toast-close-btn');
if (closeBtn) {
  closeBtn.addEventListener('click', () => {
    const toast = document.getElementById('toast-component');
    toast.classList.add('opacity-0', 'translate-y-8', 'scale-90');
  });
}
