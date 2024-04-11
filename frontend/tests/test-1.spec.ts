import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://localhost:9000/');
  await page.goto('http://localhost:9000/#/');
  await page.goto('http://localhost:9000/#/login');
  await page.getByLabel('Username').click();
  await page.getByLabel('Username').fill('alherdom');
  await page.getByLabel('Username').press('Tab');
  await page.getByLabel('Password').fill('1q2w3e4r');
  await expect(page.locator('#q-app')).toContainText('Adalogix');
  await expect(page.locator('img')).toBeVisible();
  await expect(page.locator('form')).toContainText('Forgot your password?');
  await expect(page.getByRole('button', { name: 'Log in' })).toBeVisible();
  await page.getByRole('button', { name: 'Log in' }).click();
  await expect(page.getByLabel('Expand "Alejandro Hdez"')).toContainText('Alejandro Hdez');
  await page.locator('button').filter({ hasText: 'menu' }).click();
  await page.locator('button').filter({ hasText: 'menu' }).click();
  await expect(page.getByRole('link', { name: 'HOME' })).toBeVisible();
  await page.locator('button').filter({ hasText: 'menu' }).click();
  await page.locator('button').filter({ hasText: 'menu' }).click();
  await page.getByRole('link', { name: 'INVENTORY' }).click();
  await expect(page.locator('#q-app')).toContainText('Inventory Table');
  await page.getByRole('link', { name: 'USERS' }).click();
  await expect(page.locator('#q-app')).toContainText('Users Table');
  await page.getByText('LOGOUT').click();
});
